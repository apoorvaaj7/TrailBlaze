<template>

    <StaffNavbar />

    <div class="container py-5">
        <h2 class="fw-bold mb-4">
            Registered Trekkers
        </h2>
        <div class="card shadow">
            <div class="card-body">
                <table class="table table-hover align-middle">
                    <thead class="table-success">
                        <tr>
                            <th>Name</th>
                            <th>Email</th>
                            <th>Phone</th>
                            <th>Booking Date</th>
                            <th>Payment Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr
                            v-for="trekker in trekkers" :key="trekker.booking_id">
                            <td>{{ trekker.full_name }}</td>
                            <td>{{ trekker.email }}</td>
                            <td>{{ trekker.phone }}</td>
                            <td>{{ trekker.booking_date }}</td>
                            <td>
                                <span class="badge" :class="trekker.payment_status=='Paid' ? 'bg-success' : 'bg-warning text-dark'">
                                    {{ trekker.payment_status }}
                                </span>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>

</template>

<script setup>

    import { ref,onMounted } from "vue"
    import axios from "axios"
    import { useRoute } from "vue-router"
    import StaffNavbar from "../components/StaffNavbar.vue"

    const route = useRoute()
    const trekkers = ref([])

    const loadTrekkers = async()=>{
        try{
            const response = await axios.get(`http://127.0.0.1:5000/staff/treks/${route.params.id}/trekkers`,
                {
                    headers:{
                        Authorization:"Bearer "+localStorage.getItem("token")
                    }
                })
            trekkers.value = response.data.trekkers
        }
        catch(error){
            console.log(error)
        }
    }
    onMounted(()=>{
        loadTrekkers()
    })

</script>