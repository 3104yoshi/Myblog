import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import CanSignupView from "../views/CanSignupView.vue";
import CanLoginView from "../views/CanLoginView.vue";
import NotFoundView from "../views/NotFoundView.vue";
import AuthView from "../views/AuthView.vue";
import PostView from "../views/PostView.vue";
import CanPostView from "../views/CanPostView.vue";
import LogoutView from "../views/LogoutView.vue";
import ArticleView from "../views/ArticleView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/auth/:AuthType",
    name: "auth",
    component: AuthView,
    props : (route) => ({ AuthType: route.params.AuthType }),
  },
  {
    path: "/auth/logout",
    name: "logout",
    component: LogoutView,
  },
  {
    path: "/auth/CanSignup/:SignupStatus",
    name: "CanSignup",
    component: CanSignupView,
    props : (route) => ({ SignupStatus: route.params.SignupStatus }),
  },
  {
    path: "/auth/canLogin/:LoginStatus",
    name: "CanLogin",
    component: CanLoginView,
    props : (route) => ({ SignupStatus: route.params.LoginStatus }),
  },
  {
    path: "/post",
    name: "post",
    component: PostView,
  },
  {
    path: "/canPost/:PostStatus",
    name: "canPost",
    component: CanPostView,
    props : (route) => ({ PostStatus: route.params.PostStatus }),
  },
  {
    path: "/article/:title/:content",
    name: "article",
    component: ArticleView,
    props : (route) => ({ title: route.params.title, content: route.params.content }),
  },
  {
    path: "/*",
    component: NotFoundView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
