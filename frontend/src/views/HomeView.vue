<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-white shadow-sm sticky-top">
    <div class="container">
      <router-link class="navbar-brand fw-bold text-success" to="/">
        <i class="bi bi-tree-fill me-2"></i>TrailBlaze
      </router-link>
      <button class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbar">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbar">
        <ul class="navbar-nav ms-auto align-items-center">
          <li class="nav-item">
            <a class="nav-link" href="#home">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#treks">Popular Treks</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#about">About</a>
          </li>
          <li class="nav-item ms-3">
            <router-link to="/login" class="btn btn-outline-success me-2">
              Login
            </router-link>
          </li>
          <li class="nav-item">
            <router-link to="/register" class="btn btn-success">
              Register
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <section id="home" class="hero">
    <div class="overlay">
      <div class="text-center text-white">
        <h1 class="display-3 fw-bold">
          Explore Beyond Limits
        </h1>
        <p class="lead my-4" style="color: white;">
          Discover breathtaking trekking adventures across India.
        </p>
        <router-link to="/register" class="btn btn-success btn-lg me-3">
          Get Started
        </router-link>
        <router-link to="/login" class="btn btn-outline-light btn-lg">
          Login
        </router-link>
      </div>
    </div>
  </section>
  
  <section id="treks" class="py-5 bg-light">
    <div class="container">
      <div class="text-center mb-5">
        <h2 class="fw-bold">Featured Treks</h2>
        <p class="text-muted">
        </p>
      </div>
      <div class="row">
        <div class="col-lg-4 mb-4" v-for="trek in treks" :key="trek.id">
          <div class="card border-0 shadow h-100">
            <img :src="trek.image_url" class="card-img-top" style="height:240px;object-fit:cover;">
            <div class="card-body d-flex flex-column">
              <h4 class="fw-bold">
                {{ trek.trek_name }}
              </h4>
              <p>
                <i class="fa-solid fa-location-dot text-success me-2"></i>
                {{ trek.location }}
              </p>
              <router-link to="/login" class="btn btn-success">
                Login to Book
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section id="about" class="py-5">
    <div class="container">
      <div class="text-center mb-5">
        <h2 class="fw-bold">
          Why Choose TrailBlaze?
        </h2>
      </div>
      <div class="row text-center">
        <div class="col-md-4">
          <i class="fa-solid fa-mountain fa-3x text-success mb-3"></i>
          <h4>Beautiful Treks</h4>
          <p class="text-muted">
            Discover breathtaking mountains across India.
          </p>
        </div>
        <div class="col-md-4">
          <i class="fa-solid fa-shield-heart fa-3x text-success mb-3"></i>
          <h4>Safe Adventures</h4>
          <p class="text-muted">
            Experienced guides and verified trekking routes.
          </p>
        </div>
        <div class="col-md-4">
          <i class="fa-solid fa-calendar-check fa-3x text-success mb-3"></i>
          <h4>Easy Booking</h4>
          <p class="text-muted">
            Book your next trek within minutes.
          </p>
        </div>
      </div>
    </div>
  </section>

  <section class="bg-success text-white py-5">
    <div class="container">
      <div class="row text-center">
        <div class="col-md-3">
          <h1 class="fw-bold">100+</h1>
          <p>Happy Trekkers</p>
        </div>
        <div class="col-md-3">
          <h1 class="fw-bold">50+</h1>
          <p>Treks</p>
        </div>
        <div class="col-md-3">
          <h1 class="fw-bold">20+</h1>
          <p>Experienced Guides</p>
        </div>
        <div class="col-md-3">
          <h1 class="fw-bold">100%</h1>
          <p>Adventure Guaranteed</p>
        </div>
      </div>
    </div>
  </section>
  <section class="py-5 text-center">
    <div class="container">
      <h2 class="fw-bold mb-3">
        Ready for your next adventure?
      </h2>
      <p class="lead text-muted mb-4">
        Join TrailBlaze today and explore India's most amazing treks.
      </p>
      <router-link to="/register" class="btn btn-success btn-lg">
        Start Exploring
      </router-link>
    </div>
  </section>

  <Footer />

</template>

<script setup>

  import "../assets/css/landing.css"
  import Footer from "../components/Footer.vue"

  import { ref, onMounted } from "vue"
  import { useRouter } from "vue-router"
  import axios from "axios"

  const router = useRouter()
  const treks = ref([])

  const goLogin = () => {
    router.push("/login")
  }

  const loadTreks = async () => {

    try {
      const response = await axios.get("http://127.0.0.1:5000/public-treks",
        {
          headers: {
            Authorization: "Bearer " + localStorage.getItem("token")
          }
        })
      treks.value = response.data.treks.slice(0, 3)
    }
    catch (error) {
      console.log("Login required to view treks")
    }
  }
  onMounted(() => {
    loadTreks()
  })

</script>