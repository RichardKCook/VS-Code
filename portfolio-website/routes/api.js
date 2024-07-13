const express = require('express');
const router = express.Router();

router.get('/info', (req, res) => {
  res.json({
    name: 'Your Name',
    skills: ['JavaScript', 'Node.js', 'Express', 'MongoDB'],
    background: 'Your background information'
  });
});

module.exports = router;
