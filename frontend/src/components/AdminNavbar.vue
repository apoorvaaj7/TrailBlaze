<template>
    
  <nav class="navbar navbar-expand-lg navbar-dark bg-success shadow-sm">
    <div class="container">
      <router-link class="navbar-brand fw-bold" to="/admin/dashboard"> <i class="fa-regular fa-snowflake"></i>
        TrailBlaze
      </router-link>
      <button class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbar">
        <span class="navbar-toggler-icon"></span>
      </button>
      &nbsp; &nbsp;
      <router-link class="nav-link" to="/admin/dashboard">
              Dashboard
      </router-link>
      <div class="collapse navbar-collapse" id="navbar">
        <div class="mx-auto">
            <input v-model="search" class="form-control" placeholder="Search Users, Staff or Treks..." style="width:320px" 
              @keyup.enter="searchAdmin">
        </div>
        <button class="btn btn-light ms-2"
            @click="searchAdmin">
            <i class="fa-solid fa-magnifying-glass"></i>
        </button>
        <ul class="navbar-nav ms-auto align-items-center">
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" data-bs-toggle="dropdown"> Manage </a>
            <ul class="dropdown-menu">
              <li>
                <router-link class="dropdown-item" to="/admin/manage-treks"><i class="fa-solid fa-mountain"></i>
                  Manage Treks
                </router-link>
              </li>
              <li>
                <router-link class="dropdown-item" to="/admin/manage-staff"><i class="fa-solid fa-user-tie"></i>
                  Manage Staff
                </router-link>
              </li>
              <li>
                <router-link class="dropdown-item" to="/admin/manage-trekkers"><i class="fa-solid fa-person-hiking"></i>
                  Manage Trekkers
                </router-link>
              </li>
              <li>
                <router-link class="dropdown-item" to="/admin/bookings"><i class="fa-solid fa-calendar"></i>
                  Booking Records
                </router-link>
              </li>
            </ul>
          </li>
          <li class="nav-item ms-3">
            <button class="btn btn-outline-light ms-3" @click="logout"> <i class="fa-solid fa-arrow-right-from-bracket me-2"></i>
                Logout
            </button>
          </li>
        </ul>
      </div>
    </div>
</nav>

</template>

<script setup>

  import { ref } from "vue"
  import { useRouter } from "vue-router"

  const router = useRouter()
  const search = ref("")

  const logout = () => {
      localStorage.clear()
      router.push("/login")
  }

  const searchAdmin = () => {
      router.push({
          path: "/admin/dashboard",
          query: {
              query: search.value
          }
      })
  }

</script>