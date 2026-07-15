<template>

    <AdminNavbar />

    <div class="container mt-5 py-5">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h2 class="fw-bold">
                Manage Trekkers
            </h2>
        </div>
        <table class="table table-hover align-middle">
            <thead class="table-success">
                <tr>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Phone</th>
                    <th>Bookings</th>
                    <th>Status</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                <tr
                     v-for="trekker in trekkers" :key="trekker.id">
                    <td>{{ trekker.full_name }}</td>
                    <td>{{ trekker.email }}</td>
                    <td>{{ trekker.phone }}</td>
                    <td>{{ trekker.bookings }}</td>
                    <td>
                        <span v-if="trekker.is_active" class="badge bg-success">
                            Active
                        </span>
                        <span v-else class="badge bg-danger">
                            Blacklisted
                        </span>
                    </td>
                    <td>
                        <button v-if="trekker.is_active" class="btn btn-danger btn-sm" @click="updateStatus(trekker.id,false)">
                            Blacklist
                        </button>
                        <button v-else class="btn btn-success btn-sm" @click="updateStatus(trekker.id,true)">
                            Whitelist
                        </button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>

<Footer />
</template>

<script setup>

    import { ref,onMounted } from "vue"
    import axios from "axios"
    import AdminNavbar from "../components/AdminNavbar.vue"
    import Footer from "../components/Footer.vue"

    const trekkers = ref([])

    const loadTrekkers = async()=>{
        const response = await axios.get("http://127.0.0.1:5000/admin/trekkers",
            {
                headers:{
                    Authorization:"Bearer "+localStorage.getItem("token")
                }
            })
        trekkers.value = response.data.trekkers
    }
    const updateStatus = async(user_id,is_active)=>{
        confirm(`Do you want to ${is_active ? "activate" : "deactivate"} this trekker?`)

        const response = await axios.patch(`http://127.0.0.1:5000/admin/users/${user_id}/status`,
            {
                is_active:is_active
            },
            {
                headers:{
                    Authorization:"Bearer "+localStorage.getItem("token")
                }
            })
        alert(response.data.message)
        loadTrekkers()
    }
    onMounted(()=>{
        loadTrekkers()
    })

</script>