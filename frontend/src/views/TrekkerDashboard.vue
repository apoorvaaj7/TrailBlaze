<template>

    <TrekkerNavbar />

    <div class="container mt-5 pt-5">

        <h2 class="fw-bold mb-1">

            Explore Treks

        </h2>

        <p class="text-muted mb-4">

            Discover your next adventure.

        </p>

        <div class="row">

            <div
                class="col-lg-4 col-md-6 mb-4"
                v-for="trek in treks"
                :key="trek.id">

                <div class="card shadow h-100">

                    <img
                        :src="trek.image_url"
                        class="card-img-top"
                        style="height:220px;object-fit:cover;">

                    <div class="card-body d-flex flex-column">

                        <h5 class="fw-bold">

                            {{ trek.trek_name }}

                        </h5>

                        <p class="mb-2">

                            <i class="fa-solid fa-location-dot text-success me-2"></i>

                            {{ trek.location }}

                        </p>

                        <p class="mb-2">

                            <i class="fa-solid fa-mountain text-success me-2"></i>

                            {{ trek.difficulty }}

                        </p>

                        <p class="mb-4">

                            <i class="fa-solid fa-indian-rupee-sign text-success me-2"></i>

                            {{ trek.price }}

                        </p>

                        <router-link
                            :to="'/trek/'+trek.id"
                            class="btn btn-success mt-auto">

                            View Details

                        </router-link>

                    </div>

                </div>

            </div>

        </div>

    </div>

</template>

<script setup>

import { ref,onMounted } from "vue"
import axios from "axios"

import TrekkerNavbar from "../components/TrekkerNavbar.vue"

const treks = ref([])

const loadTreks = async()=>{

    try{

        const response = await axios.get(

            "http://127.0.0.1:5000/treks",

            {

                headers:{
                    Authorization:"Bearer "+localStorage.getItem("token")
                }

            }

        )

        treks.value = response.data.treks

    }

    catch(error){

        console.log(error)

    }

}

onMounted(()=>{

    loadTreks()

})

</script>