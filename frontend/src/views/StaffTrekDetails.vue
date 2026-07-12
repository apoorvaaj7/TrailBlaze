<template>

    <StaffNavbar />

    <div class="container py-5">
        <h2 class="fw-bold text-center">
            {{ trek.trek_name }}
        </h2>
        <div class="row justify-content-center">
            <div class="col-md-6">
                <div class="card shadow mb-4">
                    <img :src="trek.image_url" class="card-img-top" style="height:350px;object-fit:cover;">
                </div>
                <hr>
                <p>
                    {{ trek.description }}
                </p>
                <hr>
                <div class="row">
                    <div class="col-md-6 mb-3">
                        <strong>
                            <i class="fa-solid fa-location-dot text-success me-2"></i>
                            Location
                        </strong>
                        <br>
                        {{ trek.location }}
                    </div>
                    <div class="col-md-6 mb-3">
                        <strong>
                            <i class="fa-solid fa-mountain text-success me-2"></i>
                            Difficulty
                        </strong>
                        <br>
                        {{ trek.difficulty }}
                    </div>
                    <div class="col-md-6 mb-3">
                        <strong>
                            <i class="fa-solid fa-users text-success me-2"></i>
                            Participants
                        </strong>
                        <br>
                        {{ trek.participants }}
                    </div>
                    <div class="col-md-6 mb-3">
                        <strong>
                            <i class="fa-solid fa-indian-rupee-sign text-success me-2"></i>
                            Price
                        </strong>
                        <br>
                        ₹ {{ trek.price }}
                    </div>
                    <div class="col-md-6 mb-3">
                        <strong>
                            <i class="fa-solid fa-calendar-days text-success me-2"></i>
                            Start Date
                        </strong>
                        <br>
                        {{ trek.start_date }}
                    </div>
                    <div class="col-md-6 mb-3">
                        <strong>
                            <i class="fa-solid fa-calendar-check text-success me-2"></i>
                            End Date
                        </strong>
                        <br>
                        {{ trek.end_date }}
                    </div>
                </div>
                <hr>
                <label class="fw-bold">
                    Available Slots
                </label>
                <div class="d-flex mb-4">
                    <input class="form-control me-2" type="number" v-model="available_slots">
                    <button class="btn btn-success" @click="updateSlots">
                        Update
                    </button>
                </div>
                <label class="fw-bold">
                    Trek Status
                </label>
                <div class="d-flex mb-4">
                    <select class="form-select me-2" v-model="status">
                        <option>Open</option>
                        <option>Closed</option>
                        <option>Ongoing</option>
                        <option>Completed</option>
                    </select>
                    <button class="btn btn-success" @click="updateStatus">
                        Update
                    </button>
                </div>
                <div class="text-center mb-5">
                    <router-link :to="'/staff/trek/' + route.params.id + '/trekkers'" class="btn btn-success px-5">
                        View Trekkers
                    </router-link>
                </div>
            </div>
        </div>
    </div>

</template>

<script setup>

    import { ref, onMounted } from "vue"
    import axios from "axios"
    import { useRoute } from "vue-router"
    import StaffNavbar from "../components/StaffNavbar.vue"

    const route = useRoute()
    const trek = ref({})
    const available_slots = ref(0)
    const status = ref("")

    const loadTrek = async () => {
        const response = await axios.get(`http://127.0.0.1:5000/staff/treks/${route.params.id}`,
            {
                headers: {
                    Authorization: "Bearer " + localStorage.getItem("token")
                }
            })
        trek.value = response.data.trek
        available_slots.value = trek.value.available_slots
        status.value = trek.value.status
    }
    const updateSlots = async () => {
        const response = await axios.patch(`http://127.0.0.1:5000/staff/treks/${route.params.id}/slots`,
            {
                available_slots: available_slots.value
            },
            {
                headers: {
                    Authorization: "Bearer " + localStorage.getItem("token")
                }
            })
        alert(response.data.message)
        loadTrek()
    }
    const updateStatus = async () => {
        const response = await axios.patch(`http://127.0.0.1:5000/staff/treks/${route.params.id}/status`,
            {
                status: status.value
            },
            {
                headers: {
                    Authorization: "Bearer " + localStorage.getItem("token")
                }
            })
        alert(response.data.message)
        loadTrek()
    }
    onMounted(() => {
        loadTrek()
    })

</script>