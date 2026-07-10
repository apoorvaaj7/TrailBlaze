<template>
  <div class="container vh-100 d-flex justify-content-center align-items-center">
    <div class="card shadow p-4" style="width:400px;">
      <h2 class="text-center mb-4">TrailBlaze</h2>
      <h5 class="text-center mb-4">Login</h5>
      <form @submit.prevent="login">
        <div class="mb-3">
          <label class="form-label">Email</label>
          <input type="email" class="form-control" v-model="email">
        </div>
        <div class="mb-3">
          <label class="form-label">Password</label>
          <input type="password" class="form-control" v-model="password">
        </div>
        <button type="submit" class="btn btn-success w-100">Login</button>
      </form>
      <hr>
      <p class="text-center">
        Don't have an account?
        <router-link to="/register">Register</router-link>
      </p>
    </div>
  </div>
</template>

<script setup>

import { ref } from "vue"
import axios from "axios"
import { useRouter } from "vue-router"

const email = ref("")
const password = ref("")

const router = useRouter()
const login = async () => {

    try{

        const response = await axios.post("http://127.0.0.1:5000/login",{
              email: email.value,
              password: password.value
        })

        localStorage.setItem( "token", response.data.access_token)
        localStorage.setItem( "role", response.data.role)

        if(response.data.role==="Admin"){
            router.push("/admin/dashboard")
        }
        else if(response.data.role==="Staff"){
            router.push("/staff/dashboard")
        }
        else{
            router.push("/dashboard")
        }
    }
    catch(error){
        alert(error.response.data.message)
    }
}

</script>