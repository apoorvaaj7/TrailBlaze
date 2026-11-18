<template>

    <div class="register-page">
        <div class="register-visual">
            <div class="visual-overlay"></div>
            <div class="visual-content">
                <router-link to="/" class="register-brand"><span class="brand-icon"><i class="fa-solid fa-compass"></i></span>TrailBlaze</router-link>
                <div class="visual-text">
                    <span class="visual-label">YOUR NEXT ADVENTURE</span>
                    <h1>Start your<br><span>next journey.</span></h1>
                    <p>Discover remarkable trails, plan unforgettable adventures and explore India's most beautiful landscapes.</p>
                </div>
                <div class="visual-bottom"><i class="fa-solid fa-quote-left"></i><span>The mountains are waiting.</span></div>
            </div>
        </div>

        <div class="register-form-area">
            <div class="register-card">
                <div class="form-header">
                    <span class="form-label">TRAILBLAZE</span>
                    <h2>Create your account</h2>
                    <p>Start exploring trails built for adventure.</p>
                </div>

                <form @submit.prevent="register">
                    <div class="form-group">
                        <label>Name</label>
                        <div class="input-wrapper">
                            <i class="fa-regular fa-user"></i>
                            <input type="text" v-model="name" placeholder="Your full name">
                        </div>
                    </div>

                    <div class="form-group">
                        <label>Email</label>
                        <div class="input-wrapper">
                            <i class="fa-regular fa-envelope"></i>
                            <input type="email" v-model="email" autocomplete="off" placeholder="you@example.com">
                        </div>
                    </div>

                    <div class="form-group">
                        <label>Phone</label>
                        <div class="input-wrapper">
                            <i class="fa-solid fa-phone"></i>
                            <input type="text" v-model="phone" placeholder="Your phone number">
                        </div>
                    </div>

                    <div class="form-group">
                        <label>Address</label>
                        <div class="input-wrapper textarea-wrapper">
                            <i class="fa-solid fa-location-dot"></i>
                            <textarea rows="2" v-model="address" placeholder="Your address"></textarea>
                        </div>
                    </div>

                    <div class="form-group">
                        <label>Password</label>
                        <div class="input-wrapper">
                            <i class="fa-solid fa-lock"></i>
                            <input type="password" v-model="password" placeholder="Create a password">
                        </div>
                    </div>

                    <button type="submit" class="register-btn">Create account <i class="fa-solid fa-arrow-right"></i></button>
                </form>

                <div class="login-prompt">
                    <span>Already have an account?</span>
                    <router-link to="/login">Log in</router-link>
                </div>
            </div>
        </div>
    </div>

</template>

<script setup>

import "../assets/css/register.css"
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