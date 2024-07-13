const { defaultFieldResolver } = require('graphql');
const { AuthenticationError } = require('@apollo/server');
const { mapSchema, getDirective, MapperKind } = require('@graphql-tools/utils');

const authDirectiveTransformer = (schema, directiveName) => {
  return mapSchema(schema, {
    [MapperKind.OBJECT_FIELD]: (fieldConfig) => {
      const authDirective = getDirective(schema, fieldConfig, directiveName)?.[0];
      if (authDirective) {
        const { resolve = defaultFieldResolver } = fieldConfig;
        fieldConfig.resolve = async function (source, args, context, info) {
          if (!context.user) {
            throw new AuthenticationError('You must be logged in');
          }
          return resolve(source, args, context, info);
        };
      }
      return fieldConfig;
    },
  });
};

module.exports = { authDirectiveTransformer };
