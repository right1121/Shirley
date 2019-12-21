import Amplify from 'aws-amplify';

Amplify.configure({
  Auth: {
    region: process.env.VUE_APP_AWS_REGION,
    identityPoolId: process.env.VUE_APP_AWS_COGNITO_ID_POOL_ID,
    userPoolId: process.env.VUE_APP_AWS_COGNITO_USERPOOL_ID,
    userPoolWebClientId: process.env.VUE_APP_AWS_COGNITO_USERPOOL_CLIENT_ID,
    authenticationFlowType: 'USER_PASSWORD_AUTH',
  },
})
