import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Dashboard from '../views/Dashboard.vue'
import DiaryCreate from "../views/DiaryCreate";
import DiaryList from "../views/DiaryList";
import DiaryDetail from "../views/DiaryDetail"
import Profile from "../views/Profile"
import UpLoad from "@/views/UpLoad.vue";

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login,
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
  },
  {
    path: "/diary-create",
    name: "DiaryCreate",
    component: DiaryCreate,
  },
  {
    path: "/diary-list",
    name: "DiaryList",
    component: DiaryList,
  },
  {
    path: "/diary-detail",
    name: "DiaryDetail",
    component: DiaryDetail,
  },
  {
    path: "/profile",
    name: "Profile",
    component: Profile,
  },
  {
    path:"/upload",
    name:"UpLoad",
    component: UpLoad,
  },
  {
    path:"/comment",
    name:"Comment",
    component: Comment,
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router