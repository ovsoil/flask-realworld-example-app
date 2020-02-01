import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Login from './views/Login.vue'
import JsonEditor from './views/JsonEditor.vue'
import JsonForm from './views/JsonForm.vue'
import Api from './views/Api.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/api',
      name: 'api',
      component: Api
    },
    {
      path: '/json',
      name: 'JsonEditor',
      component: JsonEditor
    },
    {
      path: '/form',
      name: 'JsonForm',
      component: JsonForm
      // component: () => import('./views/JsonForm.vue')
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    }
  ]
})
