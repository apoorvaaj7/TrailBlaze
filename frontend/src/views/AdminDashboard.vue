<template>

  <AdminNavbar />

  <div class="container py-5">
    <h2 class="fw-bold mb-4">Dashboard</h2>
    <div class="row g-4">
      <div class="col-md-3">
        <div class="card shadow-sm text-center p-4">
          <i class="fa-solid fa-person-hiking fs-1 text-success"></i>
          <h5 class="mt-3">Trekkers</h5>
          <h3>{{ dashboard.total_users }}</h3>
        </div>
      </div>
      <div class="col-md-3">
        <div class="card shadow-sm text-center p-4">
          <i class="fa-solid fa-user-tie fs-1 text-success"></i>
          <h5 class="mt-3">Staff</h5>
          <h3>{{ dashboard.total_staff }}</h3>
        </div>
      </div>
      <div class="col-md-3">
        <div class="card shadow-sm text-center p-4">
          <i class="fa-solid fa-mountain fs-1 text-success"></i>
          <h5 class="mt-3">Treks</h5>
          <h3>{{ dashboard.total_treks }}</h3>
        </div>
      </div>
      <div class="col-md-3">
        <div class="card shadow-sm text-center p-4">
          <i class="fa-regular fa-calendar-check fs-1 text-success"></i>
          <h5 class="mt-3">Bookings</h5>
          <h3>{{ dashboard.total_bookings }}</h3>
        </div>
      </div>
    </div>
  </div>
  
  <hr class="my-5">
    <h3 class="mb-3">Quick Actions</h3>
    <div class="row g-4">
        <div class="col-md-4">
            <router-link to="/admin/create-trek" class="btn btn-success w-50 py-3"> <i class="fa-solid fa-plus me-2"></i>
                Create Trek
            </router-link>
        </div>
        <div class="col-md-4">
            <router-link to="/admin/manage-staff" class="btn btn-outline-success w-50 py-3"> <i class="fa-solid fa-user-tie me-2"></i>
                Manage Staff
            </router-link>
        </div>
        <div class="col-md-4">
            <router-link to="/admin/manage-trekkers" class="btn btn-outline-success w-50 py-3"> <i class="fa-solid fa-person-hiking me-2"></i>
                Manage Trekkers
            </router-link>
        </div>
    </div>

    <hr class="my-5">
    <div class="d-flex justify-content-between align-items-center">
        <h3>
            Recent Treks
        </h3>
        <router-link to="/admin/manage-treks" class="btn btn-success">
            Manage Treks
        </router-link>
    </div>
    <div class="mt-4">
        <p class="text-muted">
            Recent treks will appear here.
        </p>
    </div>

</template>

<script setup>

    import { ref, onMounted } from "vue"
    import axios from "axios";
    import AdminNavbar from "../components/AdminNavbar.vue"
    
    const dashboard = ref({})

    const loadDashboard = async() => {
        try{
            const response = await axios.get("http://127.0.0.1:5000/admin/dashboard",{
                headers: {
                    Authorization: "Bearer " + localStorage.getItem("token")
                }
            })
            dashboard.value = response.data.dashboard
        }
        catch (error){
            console.log(error)
        }
    }

    onMounted(() => {
        loadDashboard()
    })

</script>

<style scoped>

.card{
    border:none;
    border-top:4px solid #198754;
    border-radius:12px;
    transition:0.3s;
}
.card:hover{
    transform:translateY(-6px);
    box-shadow:0 12px 25px rgba(0,0,0,.15);
}

</style>