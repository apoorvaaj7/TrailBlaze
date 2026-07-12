import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import AdminDashboard from '../views/AdminDashboard.vue'
import CreateTrek from '../views/CreateTrek.vue'
import ManageTreks from '../views/ManageTreks.vue'
import EditTrek from '../views/EditTrek.vue'
import CreateStaff from '../views/CreateStaff.vue'
import ManageStaff from '../views/ManageStaff.vue'
import ManageTrekkers from '../views/ManageTrekkers.vue'
import BookingRecords from '../views/BookingRecords.vue'


import StaffDashboard from '../views/StaffDashboard.vue'
import StaffTrekDetails from '../views/StaffTrekDetails.vue'
import ViewTrekkers from "../views/ViewTrekkers.vue"


const routes = [
  {
    path: '/',
    component: HomeView
  },
  {
    path: '/login',
    component: LoginView
  },
  {
    path: '/register',
    component: RegisterView
  },
  {
    path: '/admin/dashboard',
    component: AdminDashboard
  },
  {
    path: '/admin/create-trek',
    component: CreateTrek
  },
  {
    path: '/admin/manage-treks',
    component: ManageTreks
  },
  {
    path: "/admin/edit-trek/:id",
    component: EditTrek
  },
  {
    path: '/admin/create-staff',
    component: CreateStaff
  },
  {
    path: '/admin/manage-staff',
    component: ManageStaff
  },
  {
    path: '/admin/manage-trekkers',
    component: ManageTrekkers
  },
  {
    path: '/admin/bookings',
    component: BookingRecords
  },
  {
    path: '/staff/dashboard',
    component: StaffDashboard
  },
  {
    path: '/staff/trek/:id',
    component: StaffTrekDetails
  },
  {
    path:"/staff/trek/:id/trekkers",
    component:ViewTrekkers
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
