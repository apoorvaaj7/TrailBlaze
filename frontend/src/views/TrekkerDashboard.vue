<template>
    <Navbar />

    <div class="container mt-5">

        <h2 class="mb-4">
            Available Treks
        </h2>

        <div class="row">

            <TrekCard v-for="trek in treks" :key="trek.id" :trek="trek" />

        </div>

    </div>
</template>

<script setup>

import { ref, onMounted } from "vue"
import axios from "axios"

import Navbar from "../components/Navbar.vue"
import TrekCard from "../components/TrekCard.vue"

const treks = ref([])

const loadTreks = async () => {

    try {

        const response = await axios.get(
            "http://127.0.0.1:5000/treks",
            {
                headers: {
                    Authorization:
                        "Bearer " + localStorage.getItem("token")
                }
            }
        )

        treks.value = response.data.treks

    }

    catch (error) {

        console.log(error)

    }

}

onMounted(() => {

    loadTreks()

})

</script>