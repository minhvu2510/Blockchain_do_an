import Vue from 'vue'
import Router from 'vue-router'
import login from '@/views/login/login'
import contest from '@/views/Contest'
import confirm from '@/views/confirm/confirm'
import end from '@/views/end'

// in development-env not use lazy-loading, because lazy-loading too many pages will cause webpack hot update too slow. so only in production use lazy-loading;
// detail: https://panjiachen.github.io/vue-element-admin-site/#/lazy-loading

Vue.use(Router)

/** note: submenu only apppear when children.length>=1
 *   detail see  https://panjiachen.github.io/vue-element-admin-site/#/router-and-nav?id=sidebar
 **/

/**
 * hidden: true                   if `hidden:true` will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu, whatever its child routes length
 *                                if not set alwaysShow, only more than one route under the children
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noredirect           if `redirect:noredirect` will no redirct in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']     will control the page roles (you can set multiple roles)
    title: 'title'               the name show in submenu and breadcrumb (recommend set)
    icon: 'svg-name'             the icon show in the sidebar,
    noCache: true                if fasle ,the page will no be cached(default is false)
  }
 **/
export const constantRouterMap = [
  // { path: '/loading', component: _import('loading/index'), hidden: true },
  // { path: '/404', component: _import('errorPage/404'), hidden: true },
  // { path: '/401', component: _import('errorPage/401'), hidden: true },
  {
    path: '',
    component: contest,
    redirect: '',
    hidden: true
  },
  {
    path: '/login',
    component: login,
    props: true
  },
  {
    path: '/confirm',
    component: confirm,
    props: true
  },
  {
    path: '/end',
    component: end,
    props: true
  },
  // { path: '/login', component: login, hidden: true, props: true },
  // { path: '/authen', component: authen, hidden: true, props: true }
  // { path: '/dashboard', component: _import('layout/Layout'), hidden: true }
]

export default new Router({
  base: process.env.BASE_URL,
  mode: 'history', // require service support, comment this line to use hashHistory
  scrollBehavior: () => ({ y: 0 }),
  linkActiveClass: 'is-active',
  routes: constantRouterMap
})
