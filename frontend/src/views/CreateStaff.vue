<template>

    <AdminNavbar />

    <div class="container py-5">
        <h2 class="fw-bold mb-4">
            Add Staff
        </h2>
        <form @submit.prevent="createStaff" autocomplete="off">
            <div class="row">
                <div class="col-md-6 mb-3">
                    <label>Full Name</label>
                    <input v-model="full_name" class="form-control">
                </div>
                <div class="col-md-6 mb-3">
                    <label>Email</label>
                    <input type="email" v-model="email" class="form-control" autocomplete="off">
                </div>
                <div class="col-md-6 mb-3">
                    <label>Password</label>
                    <input type="password" v-model="password" class="form-control">
                </div>
                <div class="col-md-6 mb-3">
                    <label>Phone</label>
                    <input v-model="phone" class="form-control">
                </div>
                <div class="col-md-12 mb-3">
                    <label>Address</label>
                    <textarea rows="3" v-model="address" class="form-control"></textarea>
                </div>
                <div class="col-md-6 mb-3">
                    <label>Qualification</label>
                    <input v-model="qualification" class="form-control">
                </div>
                <div class="col-md-6 mb-3">
                    <label>Experience</label>
                    <input type="number" v-model="experience" class="form-control">
                </div>
                <div class="col-md-12 mb-4">
                    <label>Specialization</label>
                    <input v-model="specialization" class="form-control">
                </div>
            </div>
            <button type="submit" class="btn btn-success">
                Create Staff
            </button>
        </form>
    </div>

<Footer />
</template>

<script setup>

    import { ref } from "vue"
    import axios from "axios"
    import { useRouter } from "vue-router"
    import AdminNavbar from "../components/AdminNavbar.vue"
    import Footer from "../components/Footer.vue"

    const router = useRouter()

    const full_name = ref("")
    const email = ref("")
    const password = ref("")
    const phone = ref("")
    const address = ref("")
    const qualification = ref("")
    const experience = ref("")
    const specialization = ref("")

    const createStaff = async () => {
        try{
            const response = await axios.post("http://127.0.0.1:5000/admin/staff",
                {
                    full_name: full_name.value,
                    email: email.value,
                    password: password.value,
                    phone: phone.value,
                    address: address.value,
                    qualification: qualification.value,
                    experience: experience.value,
                    specialization: specialization.value
                },
                {
                    headers:{
                        Authorization: "Bearer " + localStorage.getItem("token")
                    }
                })

            alert(response.data.message)
            router.push("/admin/manage-staff")
        }
        catch(error){
            alert(error.response.data.message)
        }
    }

</script>