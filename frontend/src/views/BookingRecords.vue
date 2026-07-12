<template>

    <AdminNavbar />

    <div class="container py-5">
        <h2 class="fw-bold mb-4">
            Booking Records
        </h2>
        <table class="table table-hover align-middle">
            <thead class="table-success">
                <tr>
                    <th>Booking ID</th>
                    <th>Trekker</th>
                    <th>Trek</th>
                    <th>Booking Date</th>
                    <th>Booking Status</th>
                    <th>Payment Status</th>
                </tr>
            </thead>
            <tbody>
                <tr 
                    v-for="booking in booking" :key="booking.booking_id">
                    <td>{{ booking.booking_id }}</td>
                    <td>{{ booking.trekker_name }}</td>
                    <td>{{ booking.trek_name }}</td>
                    <td>{{ booking.booking_date }}</td>
                    <td>
                        <span class="badge" :class="booking.booking_status=='Booked' ? 'bg-success':'bg-danger'">
                            {{ booking.booking_status }}
                        </span>
                    </td>
                    <td>
                        <span class="badge" :class="booking.payment_status=='Paid' ? 'bg-primary':'bg-warning text-dark'">
                            {{ booking.payment_status }}
                        </span>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>

</template>

<script setup>

    import { ref,onMounted } from "vue"
    import axios from "axios"
    import AdminNavbar from "../components/AdminNavbar.vue"

    const bookings = ref([])
    const loadBookings = async()=>{
        try{
            const response = await axios.get("http://127.0.0.1:5000/admin/bookings",
                {
                    headers:{
                        Authorization:"Bearer "+localStorage.getItem("token")
                    }
                })
            bookings.value = response.data.bookings
        }
        catch(error){
            console.log(error)
        }
    }
    onMounted(()=>{
        loadBookings()
    })

</script>