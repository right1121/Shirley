<template>
  <div class="home">
    <amplify-authenticator v-bind:authConfig="authConfig"></amplify-authenticator>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'home',
  data() {
    return {
      authConfig: {
        signUpConfig: {
          usernameAttributes: 'ユーザー名',
          header: 'アカウントを作成する',
          hideAllDefaults: true,
          defaultCountryCode: '1',
          signUpFields: [
            {
              label: 'ユーザー名',
              key: 'username',
              required: true,
              displayOrder: 1,
              type: 'string'
            },
            {
              label: 'パスワード',
              key: 'password',
              required: true,
              displayOrder: 2,
              type: 'password'
            },
          ],
        }
      }
    }
  }
}
</script>
