import Vue from 'vue';
import Router from 'vue-router';
import Plants from './components/Plants.vue';
import Ping from './components/Ping.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Plants',
      component: Plants,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
});
