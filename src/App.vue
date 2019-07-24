<template>
  <v-app>
    <v-toolbar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>Vuetify</span>
        <span class="font-weight-light">MATERIAL DESIGN</span>
      </v-toolbar-title>
      <div id="nav">
        <router-link to="/">Home</router-link> |
        <router-link to="/api">API Sample</router-link> |
        <router-link to="/about">About</router-link>
      </div>
      <v-btn
        flat
        href="https://github.com/ovsoil/flask-realworld-example-app"
        target="_blank"
      >
        <span class="mr-2">Fork Me</span>
      </v-btn>
    </v-toolbar>

    <v-content>
      <router-view/>
    </v-content>
  </v-app>
</template>

<style lang="scss">
#app {
  text-align: center;
}
#nav {
  padding: 30px;
  a {
    font-weight: bold;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
#plus {
  padding: 0 20px 0 20px;
  display: inline-block;
  font-size: 50px;
  vertical-align: top;
  line-height: 100px;
}
</style>
