<template>

    <TrekkerNavbar />

    <div class="container mt-5 pt-5">
        <h2 class="fw-bold mb-4">
            My Treks
        </h2>
        <div class="row">
            <div
                class="col-lg-4 col-md-6 mb-4"
                v-for="trek in treks" :key="trek.booking_id">
                <div class="card shadow h-100">
                    <img :src="trek.image_url" class="card-img-top" style="height:220px;object-fit:cover;">
                    <div class="card-body d-flex flex-column">
                        <h5 class="fw-bold">
                            {{ trek.trek_name }}
                        </h5>
                        <p><i class="fa-solid fa-location-dot text-success me-2"></i>
                            {{ trek.location }}
                        </p>
                        <p><i class="fa-solid fa-mountain text-success me-2"></i>
                            {{ trek.difficulty }}
                        </p>
                        <p><i class="fa-solid fa-indian-rupee-sign text-success me-2"></i>
                            ₹ {{ trek.price }}
                        </p>
                        <p>
                                <i class="fa-solid fa-clock text-success me-2"></i>
                                {{ trek.duration }} Days
                            </p>
                            <p>
                                <i class="fa-solid fa-calendar text-success me-2"></i>
                                {{ trek.start_date }} - {{ trek.end_date }}
                        </p>
                        <hr>
                        <p>
                            <strong>
                                Booking Status :
                            </strong>
                            <span class="badge ms-2" :class="{
                                'bg-success':trek.booking_status=='Booked',
                                'bg-danger':trek.booking_status=='Cancelled',
                                'bg-dark':trek.booking_status=='Completed'}">
                                {{ trek.booking_status }}
                            </span>
                        </p>
                        <p>
                            <strong>
                                Payment :
                            </strong>
                            <span class="badge ms-2" :class="{
                                'bg-warning text-dark':trek.payment_status=='Pending',
                                'bg-success':trek.payment_status=='Paid',
                                'bg-info':trek.payment_status=='Refunded'}">
                                {{ trek.payment_status }}
                            </span>
                        </p>
                        <div class="mt-auto">
                            <button
                                v-if="trek.payment_status=='Pending' && trek.booking_status=='Booked'" class="btn btn-success w-100 mb-2" @click="payNow(trek.booking_id)">
                                Pay Now
                            </button>
                            <button
                                v-if="trek.booking_status=='Booked'" class="btn btn-danger w-100" @click="cancelBooking(trek.booking_id)">
                                Cancel Booking
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script setup>

    import { ref,onMounted } from "vue"
    import axios from "axios"
    import TrekkerNavbar from "../components/TrekkerNavbar.vue"

    const treks = ref([])

    const loadTreks = async()=>{
        const response = await axios.get("http://127.0.0.1:5000/my_treks",
            {
                headers:{
                    Authorization:"Bearer "+localStorage.getItem("token")
                }
            })
        treks.value = response.data.my_treks
    }
    const payNow = async(id)=>{
        const response = await axios.patch(`http://127.0.0.1:5000/bookings/${id}/pay`,
            {},
            {
                headers:{
                    Authorization:"Bearer "+localStorage.getItem("token")
                }
            })
        alert(response.data.message)
        loadTreks()
    }

    const cancelBooking = async(id)=>{
        if(!confirm("Cancel this booking?")) return

        const response = await axios.patch(`http://127.0.0.1:5000/bookings/${id}/cancel`,
            {},
            {
                headers:{
                    Authorization:"Bearer "+localStorage.getItem("token")
                }
            })
        alert(response.data.message)
        loadTreks()
    }
    onMounted(()=>{
        loadTreks()
    })

</script>