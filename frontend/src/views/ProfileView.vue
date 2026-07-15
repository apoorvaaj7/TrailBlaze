<template>

    <TrekkerNavbar />

    <div class="container py-5 mt-4">
        <div class="row justify-content-center">
            <div class="col-md-7">
                <div class="card shadow p-4">
                    <h2 class="text-center fw-bold mb-4">
                        My Profile
                    </h2>
                    <div class="mb-3">
                        <label class="form-label">Full Name</label>
                        <input class="form-control" v-model="user.full_name">
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Email</label>
                        <input class="form-control" v-model="user.email" readonly>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Phone</label>
                        <input class="form-control" v-model="user.phone">
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Address</label>
                        <textarea class="form-control" rows="3" v-model="user.address">
                        </textarea>
                    </div>
                    <div class="mb-4">
                        <label class="form-label">
                            New Password
                            <small class="text-muted">(Optional)</small>
                        </label>
                        <input type="password" class="form-control" v-model="password">
                    </div>
                    <button class="btn btn-success w-100" @click="updateProfile">
                        Update Profile
                    </button>
                </div>
            </div>
        </div>
    </div>

    <Footer />

</template>

<script setup>

    import { ref, onMounted } from "vue"
    import axios from "axios"

    import TrekkerNavbar from "../components/TrekkerNavbar.vue"
    import Footer from "../components/Footer.vue"

    const user = ref({
        full_name: "",
        email: "",
        phone: "",
        address: ""
    })
    const password = ref("")

    const loadProfile = async () => {
        try{
            const response = await axios.get("http://127.0.0.1:5000/profile",
                {
                    headers:{
                        Authorization:"Bearer "+localStorage.getItem("token")
                    }
                })
        }
        catch(error){
            console.log(error)
        }
    }
    const updateProfile = async()=>{
        try{
            const response = await axios.patch("http://127.0.0.1:5000/profile/update",
                {
                    full_name:user.value.full_name,
                    phone:user.value.phone,
                    address:user.value.address,
                    password:password.value
                },
                {
                    headers:{
                        Authorization:"Bearer "+localStorage.getItem("token")
                    }
                })
            alert(response.data.message)
            password.value = ""
        }
        catch(error){
            alert(error.response.data.message)
        }
    }
    onMounted(()=>{
        loadProfile()
    })

</script>

<style scoped>

.card{
    border-radius:18px;
}

.card-header{
    border-radius:18px 18px 0 0;
}

.form-control{
    border-radius:10px;
    padding:10px;
}

.btn{
    border-radius:10px;
    font-weight:600;
}

</style>