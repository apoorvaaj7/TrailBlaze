<template>

    <div class="login-page">
        <div class="login-visual">
            <div class="visual-overlay"></div>
            <div class="visual-content">
                <router-link to="/" class="login-brand"><span class="brand-icon"><i class="fa-solid fa-compass"></i></span>TrailBlaze</router-link>
                <div class="visual-text">
                    <span class="visual-label">WELCOME BACK</span>
                    <h1>Your next<br><span>trail awaits.</span></h1>
                    <p>Pick up where you left off and discover your next unforgettable trekking experience.</p>
                </div>
                <div class="visual-bottom"><i class="fa-solid fa-quote-left"></i><span>Find a trail that feels like yours.</span></div>
            </div>
        </div>

        <div class="login-form-area">
            <div class="login-card">
                <div class="form-header">
                    <span class="form-label">TRAILBLAZE</span>
                    <h2>Welcome back</h2>
                    <p>Log in to continue your adventure.</p>
                </div>

                <form @submit.prevent="login">
                    <div class="form-group">
                        <label>Email</label>
                        <div class="input-wrapper">
                            <i class="fa-regular fa-envelope"></i>
                            <input type="email" v-model="email" autocomplete="off" placeholder="you@example.com">
                        </div>
                    </div>

                    <div class="form-group">
                        <label>Password</label>
                        <div class="input-wrapper">
                            <i class="fa-solid fa-lock"></i>
                            <input type="password" v-model="password" placeholder="Enter your password">
                        </div>
                    </div>

                    <button type="submit" class="login-btn">Log in <i class="fa-solid fa-arrow-right"></i></button>
                </form>

                <div class="register-prompt">
                    <span>Don't have an account?</span>
                    <router-link to="/register">Create one</router-link>
                </div>
            </div>
        </div>
    </div>

</template>

<script setup>

import "../assets/css/login.css"
import { ref } from "vue"
import axios from "axios"
import { useRouter } from "vue-router"

const email = ref("")
const password = ref("")

const router = useRouter()

const login = async()=>{
    try{
        const response = await axios.post("http://127.0.0.1:5000/login",{
            email: email.value,
            password: password.value
        })

        localStorage.setItem("token",response.data.access_token)
        localStorage.setItem("role",response.data.role)

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