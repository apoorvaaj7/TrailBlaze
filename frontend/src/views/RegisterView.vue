<template>

    <div class="container py-5 d-flex justify-content-center">
        <div class="card shadow p-4" style="width:500px">
            <h2 class="text-center mb-4">
                TrailBlaze
            </h2>
            <h5 class="text-center mb-4">
                Register
            </h5>
            <form @submit.prevent="register">
                <div class="mb-3">
                    <label>Name</label>
                    <input class="form-control" v-model="name">
                </div>
                <div class="mb-3">
                    <label>Email</label>
                    <input type="email" class="form-control" v-model="email" autocomplete="off">
                </div>
                <div class="mb-3">
                    <label>Phone</label>
                    <input class="form-control" v-model="phone">
                </div>
                <div class="mb-3">
                    <label>Address</label>
                    <textarea class="form-control" rows="3" v-model="address"></textarea>
                </div>
                <div class="mb-4">
                    <label>Password</label>
                    <input type="password" class="form-control" v-model="password">
                </div>
                <button type="submit" class="btn btn-success w-100">
                    Register
                </button>
            </form>
            <hr>
            <p class="text-center">
                Already have an account?
                <router-link to="/login">
                    Login
                </router-link>
            </p>
        </div>
    </div>

</template>

<script setup>

  import { ref } from "vue"
  import axios from "axios"
  import { useRouter } from "vue-router"

  const router = useRouter()

  const name = ref("")
  const email = ref("")
  const phone = ref("")
  const address = ref("")
  const password = ref("")

  const register = async()=>{
      try{
          const response = await axios.post("http://127.0.0.1:5000/register",
              {
                  full_name: name.value,
                  email: email.value,
                  phone: phone.value,
                  address: address.value,
                  password: password.value
              })
          alert(response.data.message)
          router.push("/login")
      }
      catch(error){
          if(error.response){
              alert(error.response.data.message || error.response.data.msg)
          }
          else{
              alert("Something went wrong.")
          }
      }
  }

</script>