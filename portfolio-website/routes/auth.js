const express = require('express');
const axios = require('axios');
const User = require('../models/User');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
require('dotenv').config();

const router = express.Router();

router.post('/register', async (req, res) => {
  const { username, email, password, 'g-recaptcha-response': recaptchaResponse } = req.body;

  // Verify reCAPTCHA
  const secretKey = process.env.RECAPTCHA_SECRET_KEY;
  const verificationUrl = `https://www.google.com/recaptcha/api/siteverify?secret=${secretKey}&response=${recaptchaResponse}`;

  try {
    const response = await axios.post(verificationUrl);
    if (!response.data.success) {
      return res.status(400).send('Failed reCAPTCHA verification');
    }

    // Continue with user registration
    const user = new User({ username, email, password });
    await user.save();
    res.status(201).send('User registered');
  } catch (error) {
    res.status(400).send(error);
  }
});

router.post('/login', async (req, res) => {
  const { email, password } = req.body;
  try {
    const user = await User.findOne({ email });
    if (!user) return res.status(400).send('User not found');

    const isMatch = await bcrypt.compare(password, user.password);
    if (!isMatch) return res.status(400).send('Invalid credentials');

    const token = jwt.sign({ id: user._id }, process.env.JWT_SECRET, { expiresIn: '1h' });
    res.json({ token });
  } catch (error) {
    res.status(400).send(error);
  }
});

module.exports = router;
