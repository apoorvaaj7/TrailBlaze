<template>

    <TrekkerNavbar />

    <main class="trekker-page">
        <section class="trekker-header">
            <div>
                <span class="section-label">EXPLORE</span>
                <h1>Find your next trail.</h1>
                <p>Discover trekking experiences across India's most beautiful landscapes.</p>
            </div>
            <div class="trek-count" v-if="treks.length > 0">
                <strong>{{ treks.length }}</strong>
                <span>trails available</span>
            </div>
        </section>

        <section class="treks-section">
            <div class="trek-grid" v-if="treks.length > 0">
                <article class="trek-card" v-for="trek in treks" :key="trek.id">
                    <div class="trek-image">
                        <img :src="trek.image_url" :alt="trek.trek_name">
                        <span class="difficulty">{{ trek.difficulty }}</span>
                    </div>
                    <div class="trek-content">
                        <div class="trek-location"><i class="fa-solid fa-location-dot"></i>{{ trek.location }}</div>
                        <h3>{{ trek.trek_name }}</h3>
                        <div class="trek-meta">
                            <span><i class="fa-solid fa-mountain"></i>{{ trek.difficulty }}</span>
                            <span class="trek-price">₹{{ trek.price }}</span>
                        </div>
                        <router-link :to="'/trek/'+trek.id" class="view-trek">View trek <i class="fa-solid fa-arrow-right"></i></router-link>
                    </div>
                </article>
            </div>

            <div v-else class="empty-state">
                <div class="empty-icon"><i class="fa-solid fa-mountain"></i></div>
                <span class="section-label">NOTHING HERE YET</span>
                <h2>No treks found</h2>
                <p>Try searching with another trek name, location, or difficulty.</p>
            </div>
        </section>
    </main>

    <Footer />

</template>

<script setup>

import "../assets/css/trekker.css"
import { ref,onMounted,watch } from "vue"
import axios from "axios"
import { useRoute } from "vue-router"
import TrekkerNavbar from "../components/TrekkerNavbar.vue"
import Footer from "../components/Footer.vue"

const treks = ref([])
const route = useRoute()

const loadTreks = async()=>{
    try{
        const query = route.query.query || ""
        const difficulty = route.query.difficulty || "All"
        let url = "http://127.0.0.1:5000/treks"

        if(query || difficulty!="All"){
            url = `http://127.0.0.1:5000/treks/search?query=${query}&difficulty=${difficulty}`
        }

        const response = await axios.get(url,{
            headers:{
                Authorization:"Bearer "+localStorage.getItem("token")
            }
        })
        treks.value = response.data.treks
    }
    catch(error){
        console.log(error)
    }
}

onMounted(loadTreks)

watch(
    ()=>route.query,
    ()=>loadTreks()
)

</script>