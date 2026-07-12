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

  import { useRouter } from 'vue-router';

  const router = useRouter()
  const logout = () => {
    localStorage.clear()
    router.push("/login")
  }

</script>