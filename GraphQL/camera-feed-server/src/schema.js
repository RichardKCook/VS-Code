const { gql } = require('apollo-server');

const typeDefs = gql`
  type Query {
    cameraFeed(id: ID!): CameraFeed
    insights(cameraFeedId: ID!): [Insight]
  }

  type Mutation {
    login(username: String!, password: String!): AuthPayload
    uploadCameraFeed(input: UploadCameraFeedInput!): CameraFeed
  }

  input UploadCameraFeedInput {
    customerId: ID!
    feedType: FeedType!
    data: String! # Assume data is a base64 encoded string for simplicity
    timestamp: String!
  }

  enum FeedType {
    RGB
    INFRARED
  }

  type CameraFeed {
    id: ID!
    customerId: ID!
    feedType: FeedType!
    encryptedData: String! # Encrypted data
    timestamp: String!
    insights: [Insight]
  }

  type Insight {
    id: ID!
    cameraFeedId: ID!
    description: String!
    timestamp: String!
  }

  type AuthPayload {
    token: String!
    user: User!
  }

  type User {
    id: ID!
    username: String!
  }
`;

module.exports = typeDefs;
