<template>

    <AdminNavbar />

    <div class="container mt-5 py-5">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h2 class="fw-bold">
                Manage Staff
            </h2>
            <router-link to="/admin/create-staff" class="btn btn-success"><i class="fa-solid fa-user-plus me-2"></i>
                Add Staff
            </router-link>
        </div>
        <table class="table table-hover align-middle">
            <thead class="table-success">
                <tr>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Qualification</th>
                    <th>Experience (In Years)</th>
                    <th>Specialization</th>
                    <th>Status</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                <tr
                    v-for="staff in staffs"
                    :key="staff.id">
                    <td>{{ staff.full_name }}</td>
                    <td>{{ staff.email }}</td>
                    <td>{{ staff.qualification }}</td>
                    <td>{{ staff.experience }}</td>
                    <td>{{ staff.specialization }}</td>
                    <td>
                        <span v-if="staff.is_active" class="badge bg-success">
                            Active
                        </span>
                        <span v-else class="badge bg-danger">
                            Inactive
                        </span>
                    </td>
                    <td>
                        <button v-if="staff.is_active" class="btn btn-danger btn-sm" @click="updateStatus(staff.user_id,false)">
                            Deactivate
                        </button>
                        <button v-else class="btn btn-success btn-sm" @click="updateStatus(staff.user_id,true)">
                            Activate
                        </button>
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

    const staffs = ref([])
    const loadStaff = async () => {
        try{
            const response = await axios.get("http://127.0.0.1:5000/admin/staff",
                {
                    headers:{
                        Authorization:"Bearer "+localStorage.getItem("token")
                    }
                })
            staffs.value = response.data.staff
        }
        catch(error){
            console.log(error)
        }
    }
    const updateStatus = async(user_id,is_active)=>{
        confirm(`Do you want to ${is_active ? "activate" : "deactivate"} this staff member?`)
        try{
            const response = await axios.patch(`http://127.0.0.1:5000/admin/users/${user_id}/status`,
                {
                    is_active:is_active
                },
                {
                    headers:{
                        Authorization:"Bearer "+localStorage.getItem("token")
                    }
                }
            )
            alert(response.data.message)
            loadStaff()
        }
        catch(error){
            alert(error.response.data.message)
        }
    }
    onMounted(()=>{
        loadStaff()
    })

</script>