const { AuthenticationError } = require('apollo-server');
const { v4: uuidv4 } = require('uuid');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');
const crypto = require('crypto');

// Sample data
const cameraFeeds = [];
const insights = [];
const users = [
  { id: '1', username: 'testuser', password: bcrypt.hashSync('password', 10) },
];

// JWT Secret
const JWT_SECRET = 'your_jwt_secret';

// Encryption key and IV
const ENCRYPTION_KEY = crypto.randomBytes(32); // Must be 256 bits (32 bytes)
const IV_LENGTH = 16; // For AES, this is always 16

// Encrypt function
const encrypt = (text) => {
  const iv = crypto.randomBytes(IV_LENGTH);
  const cipher = crypto.createCipheriv('aes-256-cbc', Buffer.from(ENCRYPTION_KEY), iv);
  let encrypted = cipher.update(text);
  encrypted = Buffer.concat([encrypted, cipher.final()]);
  return iv.toString('hex') + ':' + encrypted.toString('hex');
};

// Decrypt function
const decrypt = (text) => {
  const textParts = text.split(':');
  const iv = Buffer.from(textParts.shift(), 'hex');
  const encryptedText = Buffer.from(textParts.join(':'), 'hex');
  const decipher = crypto.createDecipheriv('aes-256-cbc', Buffer.from(ENCRYPTION_KEY), iv);
  let decrypted = decipher.update(encryptedText);
  decrypted = Buffer.concat([decrypted, decipher.final()]);
  return decrypted.toString();
};

// Middleware to verify JWT
const getUser = (token) => {
  try {
    if (token) {
      return jwt.verify(token, JWT_SECRET);
    }
    return null;
  } catch (err) {
    return null;
  }
};

// Define the resolvers
const resolvers = {
  Query: {
    cameraFeed: (parent, args, context) => {
      if (!context.user) {
        throw new AuthenticationError('You must be logged in');
      }
      const feed = cameraFeeds.find(feed => feed.id === args.id);
      if (feed) {
        return { ...feed, encryptedData: decrypt(feed.encryptedData) };
      }
      return null;
    },
    insights: (parent, args, context) => {
      if (!context.user) {
        throw new AuthenticationError('You must be logged in');
      }
      return insights.filter(insight => insight.cameraFeedId === args.cameraFeedId);
    },
  },
  Mutation: {
    login: async (parent, { username, password }) => {
      const user = users.find(user => user.username === username);
      if (!user || !await bcrypt.compare(password, user.password)) {
        throw new AuthenticationError('Invalid credentials');
      }
      const token = jwt.sign({ userId: user.id }, JWT_SECRET, { expiresIn: '1d' });
      return { token, user };
    },
    uploadCameraFeed: (parent, { input }, context) => {
      if (!context.user) {
        throw new AuthenticationError('You must be logged in');
      }
      const encryptedData = encrypt(input.data);
      const newFeed = { id: uuidv4(), ...input, data: undefined, encryptedData, insights: [] };
      cameraFeeds.push(newFeed);
      // Simulate processing and generating insights
      const newInsight = {
        id: uuidv4(),
        cameraFeedId: newFeed.id,
        description: "Simulated insight for demonstration purposes",
        timestamp: new Date().toISOString(),
      };
      insights.push(newInsight);
      newFeed.insights.push(newInsight);
      return newFeed;
    },
  },
  CameraFeed: {
    insights: (feed) => insights.filter(insight => insight.cameraFeedId === feed.id),
  },
};

module.exports = resolvers;
