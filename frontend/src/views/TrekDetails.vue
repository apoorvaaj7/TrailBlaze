<template>

    <TrekkerNavbar />

    <div class="container mt-5 pt-5">

        <h2 class="fw-bold text-center mb-4">

            Trek Details

        </h2>

        <div class="row justify-content-center">

            <div class="col-lg-8">

                <div class="card shadow mb-4">

                    <img
                        :src="trek.image_url"
                        class="card-img-top"
                        style="height:420px;object-fit:cover;">

                </div>

                <h2 class="fw-bold text-center">

                    {{ trek.trek_name }}

                </h2>

                <p class="text-center text-muted">

                    {{ trek.location }} • {{ trek.difficulty }} • {{ trek.duration }} Days

                </p>

                <hr>

                <h5>Description</h5>

                <p>

                    {{ trek.description }}

                </p>

                <hr>

                <div class="row">

                    <div class="col-md-6 mb-3">

                        <strong>

                            <i class="fa-solid fa-location-dot text-success me-2"></i>

                            Location

                        </strong>

                        <br>

                        {{ trek.location }}

                    </div>

                    <div class="col-md-6 mb-3">

                        <strong>

                            <i class="fa-solid fa-mountain text-success me-2"></i>

                            Difficulty

                        </strong>

                        <br>

                        {{ trek.difficulty }}

                    </div>

                    <div class="col-md-6 mb-3">

                        <strong>

                            <i class="fa-solid fa-indian-rupee-sign text-success me-2"></i>

                            Price

                        </strong>

                        <br>

                        ₹ {{ trek.price }}

                    </div>

                    <div class="col-md-6 mb-3">

                        <strong>

                            <i class="fa-solid fa-users text-success me-2"></i>

                            Available Slots

                        </strong>

                        <br>

                        {{ trek.available_slots }}

                    </div>

                    <div class="col-md-6 mb-3">

                        <strong>

                            <i class="fa-solid fa-calendar-days text-success me-2"></i>

                            Start Date

                        </strong>

                        <br>

                        {{ trek.start_date }}

                    </div>

                    <div class="col-md-6 mb-3">

                        <strong>

                            <i class="fa-solid fa-calendar-check text-success me-2"></i>

                            End Date

                        </strong>

                        <br>

                        {{ trek.end_date }}

                    </div>

                </div>

                <div class="text-center mt-4 mb-5">

                    <button
                        class="btn btn-success px-5"
                        @click="bookTrek">

                        Book Trek

                    </button>

                </div>

            </div>

        </div>

    </div>

</template>

<script setup>

import { ref,onMounted } from "vue"
import axios from "axios"

import { useRoute,useRouter } from "vue-router"

import TrekkerNavbar from "../components/TrekkerNavbar.vue"

const route = useRoute()

const router = useRouter()

const trek = ref({})

const loadTrek = async()=>{

    try{

        const response = await axios.get(

            `http://127.0.0.1:5000/treks/${route.params.id}`,

            {

                headers:{
                    Authorization:"Bearer "+localStorage.getItem("token")
                }

            }

        )

        trek.value = response.data.trek

    }

    catch(error){

        console.log(error)

    }

}

const bookTrek = async()=>{

    try{

        const response = await axios.post(

            `http://127.0.0.1:5000/treks/${route.params.id}`,

            {},

            {

                headers:{
                    Authorization:"Bearer "+localStorage.getItem("token")
                }

            }

        )

        alert(response.data.message)

        router.push("/my-treks")

    }

    catch(error){

        alert(error.response.data.message)

    }

}

onMounted(()=>{

    loadTrek()

})

</script>