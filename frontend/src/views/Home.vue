<template>
  <div class="home">
    <v-toolbar color="white">
      <v-toolbar-title v-text="title"></v-toolbar-title>
    </v-toolbar>
    <v-content>
      <section>
        <v-parallax src="@/assets/hero.jpg" height="600">
          <v-layout
            column
            align-center
            justify-center
            class="white--text"
          >
            <h1 class="white--text mb-2 display-1 text-center">大切な車両の管理サイト</h1>
            <div class="subheading mb-4 text-center">鉄道模型管理サイト『SHIRLEY DEPO』</div>
          </v-layout>
        </v-parallax>
      </section>

      <section>
        <v-layout
          column
          wrap
          class="my-12"
          align-center
        >
          <v-flex xs12 sm4 class="my-4">
            <div class="text-center">
              <span class="subheading">
                Service
              </span>
              <h2 class="headline">機能</h2>
            </div>
          </v-flex>
          <v-flex xs12>
            <v-container grid-list-xl>
              <v-layout row wrap align-center>
                <v-flex xs12 md12>
                  <v-card flat class="transparent">
                    <v-card-title primary-title class="layout justify-center">
                      <div class="headline text-center">保有車両確認</div>
                    </v-card-title>
                    <v-card-text>
                      保有している車両を一覧で表示。自分がどのような車両を保有しているのか確認できます。
                    </v-card-text>
                  </v-card>
                </v-flex>
              </v-layout>
            </v-container>
          </v-flex>
        </v-layout>
      </section>
      <section>
        <amplify-authenticator v-bind:authConfig="authConfig"></amplify-authenticator>
      </section>
      <v-footer color="blue darken-2">
      </v-footer>
    </v-content>
  </div>
  
</template>

<script>
// @ is an alias to /src

export default {
  name: 'home',
  data() {
    return {
      title: 'SHIRLEY DEPO',
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
