<template>

    <AdminNavbar />

    <div class="container py-5">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h2 class="fw-bold">
                Manage Trek
            </h2>
            <router-link to="/admin/create-trek" class="btn btn-success"> <i class="fa-solid fa-plus me-2"></i>
                Create Trek
            </router-link>
        </div>
        <table class="table table-striped table-hover align-middle">
            <thead class="table-success">
                <tr>
                    <th>Name</th>
                    <th>Location</th>
                    <th>Staff</th>
                    <th>Difficulty</th>
                    <th>Price</th>
                    <th>Slots</th>
                    <th>Status</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="trek in treks" :key="trek.id">
                    <td>{{ trek.trek_name }}</td>
                    <td>{{ trek.location }}</td>
                    <td>{{ trek.staff_name }}</td>
                    <td>{{ trek.difficulty }}</td>
                    <td>₹ {{ trek.price }}</td>
                    <td>{{ trek.available_slots }}</td>
                    <td>{{ trek.status }}</td>
                    <td>
                        <router-link :to="'/admin/edit-trek/' + trek.id" class="btn btn-warning btn-sm me-2">
                            Edit
                        </router-link>
                        <button class="btn btn-danger btn-sm" @click="deleteTrek(trek.id)">
                            Delete
                        </button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>

<Footer />
</template>
<script setup>

    import { ref, onMounted } from "vue"
    import axios from "axios"
    import AdminNavbar from "../components/AdminNavbar.vue"
    import Footer from "../components/Footer.vue"

    const treks = ref([])
    const loadTreks = async () => {
        try {
            const response = await axios.get("http://127.0.0.1:5000/admin/treks", {
                headers: {
                    Authorization: "Bearer " + localStorage.getItem("token")
                }
            })
            treks.value = response.data.treks
        }
        catch (error) {
            console.log(error)
        }
    }
    const deleteTrek = async (id) => {
        if (!confirm("Delete this trek?")) return
        try {
            await axios.delete( `http://127.0.0.1:5000/admin/treks/${id}`, {
                    headers: { Authorization: "Bearer " + localStorage.getItem("token")}
                }
            )
            alert("Trek deleted successfully.")
            loadTreks()
        }
        catch (error) {
            alert(error.response.data.message)
        }
    }
    onMounted(() => {
        loadTreks()
    })

</script>

