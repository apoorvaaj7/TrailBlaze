<template>

    <AdminNavbar />

    <div class="container py-5">
        <h2 class="fw-bold mb-4">
            All Treks
        </h2>

        <div class="row">

            <div
                class="col-md-4 mb-4"
                v-for="trek in treks"
                :key="trek.id"
            >

                <div class="card shadow h-100">

                    <img
                        :src="trek.image_url"
                        class="card-img-top"
                        style="height:220px; object-fit:cover"
                    >

                    <div class="card-body">

                        <h4>{{ trek.trek_name }}</h4>

                        <p>
                            <strong>Location:</strong>
                            {{ trek.location }}
                        </p>

                        <p>
                            <strong>Difficulty:</strong>
                            {{ trek.difficulty }}
                        </p>

                        <p>
                            <strong>Duration:</strong>
                            {{ trek.duration }} Days
                        </p>

                        <p>
                            <strong>Price:</strong>
                            ₹ {{ trek.price }}
                        </p>

                        <p>
                            <strong>Slots:</strong>
                            {{ trek.available_slots }}
                        </p>

                        <p>
                            <strong>Staff:</strong>
                            {{ trek.staff_name }}
                        </p>

                        <span
                            class="badge"
                            :class="{
                                'bg-success': trek.status=='Open',
                                'bg-warning text-dark': trek.status=='Ongoing',
                                'bg-secondary': trek.status=='Completed',
                                'bg-danger': trek.status=='Closed'
                            }"
                        >
                            {{ trek.status }}
                        </span>

                    </div>

                </div>

            </div>

        </div>

    </div>

    <Footer />

</template>

<script setup>

import { ref,onMounted } from "vue"
import axios from "axios"

import AdminNavbar from "../components/AdminNavbar.vue"
import Footer from "../components/Footer.vue"

const treks = ref([])

const loadTreks = async()=>{

    try{

        const response = await axios.get(
            "http://127.0.0.1:5000/admin/treks",
            {
                headers:{
                    Authorization:"Bearer "+localStorage.getItem("token")
                }
            }
        )

        treks.value=response.data.treks

    }

    catch(error){

        console.log(error)

    }

}

onMounted(()=>{

    loadTreks()

})

</script>