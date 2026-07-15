<template>

    <AdminNavbar />

    <div class="container py-5">
        <h2 class="fw-bold mb-4">
            Dashboard
        </h2>
        <div class="row g-4">
            <div class="col-md-3">
                <div class="card shadow-sm text-center p-4">
                    <i class="fa-solid fa-person-hiking fs-1 text-success"></i>
                    <h5 class="mt-3">
                        Trekkers
                    </h5>
                    <h3>
                        {{ dashboard.total_users }}
                    </h3>
                </div>
            </div>
            <div class="col-md-3">
                <div class="card shadow-sm text-center p-4">
                    <i class="fa-solid fa-user-tie fs-1 text-success"></i>
                    <h5 class="mt-3">
                        Staff
                    </h5>
                    <h3>
                        {{ dashboard.total_staff }}
                    </h3>
                </div>
            </div>
            <div class="col-md-3">
                <div class="card shadow-sm text-center p-4">
                    <i class="fa-solid fa-mountain fs-1 text-success"></i>
                    <h5 class="mt-3">
                        Treks
                    </h5>
                    <h3>
                        {{ dashboard.total_treks }}
                    </h3>
                </div>
            </div>
            <div class="col-md-3">
                <div class="card shadow-sm text-center p-4">
                    <i class="fa-regular fa-calendar-check fs-1 text-success"></i>
                    <h5 class="mt-3">
                        Bookings
                    </h5>
                    <h3>
                        {{ dashboard.total_bookings }}
                    </h3>
                </div>
            </div>
        </div>

        <div v-if="route.query.query">
            <h3 class="mb-3">
                Search Results
            </h3>
            <h5>Users</h5>
            <ul class="list-group mb-4">
                <li class="list-group-item" v-for="user in users" :key="user.id">
                    {{ user.full_name }} ({{ user.role }}) - {{ user.email }}
                </li>
            </ul>
            <h5>Treks</h5>
            <ul class="list-group">
                <li class="list-group-item" v-for="trek in treks" :key="trek.id">
                    {{ trek.trek_name }} - {{ trek.location }}
                </li>
            </ul>
        </div>

        <div v-else>
            <hr class="my-5">
            <div class="d-flex justify-content-between align-items-center mb-4">
                <h3 class="fw-bold">
                    Recent Treks
                </h3>
                <router-link to="/admin/all-treks" class="btn btn-success">
                    View All Treks
                </router-link>
            </div>
            <div
                v-if="dashboard.recent_treks && dashboard.recent_treks.length" class="row">
                <div
                    class="col-lg-4 mb-4"
                    v-for="trek in dashboard.recent_treks" :key="trek.id">
                    <div class="card shadow h-100">
                        <img
                            :src="trek.image_url" class="card-img-top" style="height:220px;object-fit:cover;">
                        <div class="card-body d-flex flex-column">
                            <h5 class="fw-bold">
                                {{ trek.trek_name }}
                            </h5>
                            <p class="mb-2">
                                <i class="fa-solid fa-location-dot text-success me-2"></i>
                                {{ trek.location }}
                            </p>
                            <p class="mb-2">
                                <i class="fa-solid fa-mountain text-success me-2"></i>
                                {{ trek.difficulty }}
                            </p>
                            <p class="mb-2">
                                <i class="fa-solid fa-indian-rupee-sign text-success me-2"></i>
                                ₹ {{ trek.price }}
                            </p>
                            <p class="mb-3">
                                <span class="badge" :class="{
                                        'bg-success': trek.status=='Open',
                                        'bg-warning text-dark': trek.status=='Ongoing',
                                        'bg-danger': trek.status=='Closed',
                                        'bg-dark': trek.status=='Completed'
                                    }">
                                    {{ trek.status }}
                                </span>
                            </p>
                            <router-link :to="'/admin/edit-trek/' + trek.id" class="btn btn-success mt-auto">
                                Edit Trek
                            </router-link>
                        </div>
                    </div>
                </div>
            </div>
            <div
                v-else class="text-center py-5">
                <i class="fa-solid fa-mountain fa-4x text-secondary mb-3"></i>
                <h4>
                    No Treks Available
                </h4>
                <p class="text-muted">
                    Create your first trek to get started.
                </p>
                <router-link to="/admin/create-trek" class="btn btn-success">
                    Create Trek
                </router-link>
            </div>
        </div>
    </div>

<Footer />

</template>

<script setup>

    import { ref, onMounted, watch } from "vue"
    import axios from "axios"
    import AdminNavbar from "../components/AdminNavbar.vue"
    import Footer from "../components/Footer.vue"
    import { useRoute } from "vue-router"

    const route = useRoute()
    const dashboard = ref({})
    const users = ref([])
    const treks = ref([])
    

    const loadDashboard = async() => {
        try{
            const response = await axios.get("http://127.0.0.1:5000/admin/dashboard",
                {
                    headers:{
                        Authorization:"Bearer "+localStorage.getItem("token")
                    }
                })
            dashboard.value = response.data.dashboard
        }
        catch(error){
            console.log(error)
        }
    }

    const searchAdmin = async () => {

        try{
            const query = route.query.query || ""

            if(query==""){
                loadDashboard()
                return
            }
            const response = await axios.get(`http://127.0.0.1:5000/admin/search?query=${query}`,
                {
                    headers:{
                        Authorization:"Bearer "+localStorage.getItem("token")
                    }
                })
            users.value = response.data.users
            treks.value = response.data.treks
        }
        catch(error){
            console.log(error)
        }
    }

   onMounted(()=>{
        if(route.query.query){
            searchAdmin()
        }
        else{
            loadDashboard()
        }
    })
    watch(
        ()=>route.query,
        ()=>{
            if(route.query.query){
                searchAdmin()
            }
            else{
                loadDashboard()
            }
        }
    )

</script>

<style scoped>

    .card{
        border:none;
        border-top:4px solid #198754;
        border-radius:12px;
        transition:.3s;
    }
    .card:hover{
        transform:translateY(-6px);
        box-shadow:0 12px 25px rgba(0,0,0,.15);
    }

</style>