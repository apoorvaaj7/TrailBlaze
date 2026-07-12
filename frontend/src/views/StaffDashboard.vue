<template>

    <StaffNavbar />

    <div class="container py-5">
        <h2 class="fw-bold mb-4">
            Staff Dashboard
        </h2>
        <div class="row mb-5">
            <div class="col-md-6">
                <div class="card shadow-sm text-center p-4">
                    <i class="fa-solid fa-map-location-dot fs-1 text-success"></i>
                    <h5 class="mt-3">
                        Assigned Treks
                    </h5>
                    <h2>{{ dashboard.assigned_treks }}</h2>
                </div>
            </div>
            <div class="col-md-6">
                <div class="card shadow-sm text-center p-4">
                    <i class="fa-solid fa-person-hiking fs-1 text-success"></i>
                    <h5 class="mt-3">
                        Registered Trekkers
                    </h5>
                    <h2>{{ dashboard.registered_trekkers }}</h2>
                </div>
            </div>
        </div>
        <h3 class="fw-bold mb-4">
            Assigned Treks
        </h3>
        <div
            v-if="dashboard.treks.length==0" class="text-center py-5">
            <i class="fa-solid fa-mountain fs-1 text-secondary"></i>
            <h4 class="mt-3">
                No Treks Assigned
            </h4>
            <p class="text-muted">
                You currently don't have any assigned treks.
            </p>
        </div>
        <div class="row" v-else>
            <div class="col-md-3 mb-4"
                v-for="trek in dashboard.treks" :key="trek.id">
                <div class="card shadow h-100">
                    <img :src="trek.image_url" class="card-img-top" style="height:220px;object-fit:cover;">

                    <div class="card-body">
                        <h5 class="fw-bold">
                            {{ trek.trek_name }}
                        </h5>
                        <p><i class="fa-solid fa-location-dot text-success"></i>
                            {{ trek.location }}
                        </p>
                        <p>
                            {{ trek.difficulty }}
                        </p>
                        <p>
                            <span class="badge bg-success">
                                {{ trek.status }}
                            </span>
                        </p>
                        <router-link
                            :to="'/staff/trek/'+trek.id" class="btn btn-success w-100">
                            View Details
                        </router-link>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script setup>

    import { ref,onMounted } from "vue"
    import axios from "axios"
    import StaffNavbar from "../components/StaffNavbar.vue"

    const dashboard = ref({
        treks:[]
    })
    const loadDashboard = async()=>{
        try{
            const response = await axios.get("http://127.0.0.1:5000/staff/dashboard",
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
    onMounted(()=>{
        loadDashboard()
    })

</script>