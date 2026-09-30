<template>

  <!-- ================= NAVBAR ================= -->
  <nav class="tb-navbar">

    <div class="tb-nav-container">

      <!-- Brand -->
      <router-link to="/" class="tb-brand">

        <span class="brand-mark">
          <i class="fa-solid fa-compass"></i>
        </span>

        <span>TrailBlaze</span>

      </router-link>


      <!-- Desktop Navigation -->
      <div class="tb-nav-links">

        <a href="#home" class="tb-nav-link">
          Home
        </a>

        <a href="#treks" class="tb-nav-link">
          Explore Treks
        </a>

        <a href="#about" class="tb-nav-link">
          About
        </a>

        <router-link to="/login" class="tb-login">
          Login
        </router-link>

        <router-link to="/register" class="tb-start-btn">
          Get Started
          <i class="fa-solid fa-arrow-right"></i>
        </router-link>

      </div>


      <!-- Mobile Menu Button -->
      <button
        class="tb-mobile-toggle"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#mobileNav"
      >
        <i class="fa-solid fa-bars"></i>
      </button>

    </div>


    <!-- Mobile Navigation -->
    <div class="collapse tb-mobile-nav" id="mobileNav">

      <a href="#home" class="tb-mobile-link">
        Home
      </a>

      <a href="#treks" class="tb-mobile-link">
        Explore Treks
      </a>

      <a href="#about" class="tb-mobile-link">
        About
      </a>

      <router-link to="/login" class="tb-mobile-link">
        Login
      </router-link>

      <router-link to="/register" class="tb-mobile-start">
        Get Started
      </router-link>

    </div>

  </nav>


  <!-- ================= HERO ================= -->
  <section id="home" class="tb-hero">

    <div class="tb-hero-overlay"></div>


    <div class="tb-hero-content">

      <div class="tb-hero-eyebrow">

        <span></span>

        EXPLORE INDIA'S TRAILS

      </div>


      <h1>
        Find your
        <span>next trail.</span>
      </h1>


      <p>
        Curated trekking experiences across India's most
        breathtaking landscapes.
      </p>


      <div class="tb-hero-actions">

        <router-link
          to="/register"
          class="tb-primary-btn"
        >
          Explore Treks

          <i class="fa-solid fa-arrow-right"></i>

        </router-link>


        <a
          href="#treks"
          class="tb-secondary-btn"
        >
          View featured treks
        </a>

      </div>

    </div>


    <!-- ================= FLOATING VALUE PANEL ================= -->
    <div class="tb-value-panel">


      <div class="tb-value-item">

        <div class="tb-value-icon">
          <i class="fa-solid fa-mountain"></i>
        </div>

        <div>

          <h3>
            Curated trails
          </h3>

          <p>
            Handpicked trekking experiences
          </p>

        </div>

      </div>


      <div class="tb-value-divider"></div>


      <div class="tb-value-item">

        <div class="tb-value-icon">
          <i class="fa-solid fa-compass"></i>
        </div>

        <div>

          <h3>
            Experienced guides
          </h3>

          <p>
            People who know every trail
          </p>

        </div>

      </div>


      <div class="tb-value-divider"></div>


      <div class="tb-value-item">

        <div class="tb-value-icon">
          <i class="fa-solid fa-calendar-check"></i>
        </div>

        <div>

          <h3>
            Simple booking
          </h3>

          <p>
            Plan your adventure with ease
          </p>

        </div>

      </div>

    </div>

  </section>


  <!-- ================= FEATURED TREKS ================= -->
  <section id="treks" class="tb-treks-section">

    <div class="tb-section-container">


      <div class="tb-section-heading">

        <div>

          <span class="tb-section-label">
            EXPLORE
          </span>

          <h2>
            Featured treks
          </h2>

        </div>


        <p>
          Discover some of the experiences waiting
          beyond the ordinary.
        </p>

      </div>


      <!-- Trek Cards -->
      <div
        v-if="treks.length > 0"
        class="tb-trek-grid"
      >

        <div
          v-for="trek in treks"
          :key="trek.id"
          class="tb-trek-card"
        >

          <!-- Trek Image -->
          <div class="tb-trek-image-wrapper">

            <img
              :src="trek.image_url"
              :alt="trek.trek_name"
              class="tb-trek-image"
            />

            <div class="tb-image-overlay"></div>

            <span class="tb-trek-tag">
              Featured
            </span>

          </div>


          <!-- Trek Information -->
          <div class="tb-trek-content">

            <div class="tb-trek-location">

              <i class="fa-solid fa-location-dot"></i>

              {{ trek.location }}

            </div>


            <h3>
              {{ trek.trek_name }}
            </h3>


            <p>
              Discover an unforgettable trekking
              experience surrounded by breathtaking
              landscapes.
            </p>


            <router-link
              to="/login"
              class="tb-trek-link"
            >

              View trek

              <i class="fa-solid fa-arrow-right"></i>

            </router-link>

          </div>

        </div>

      </div>


      <!-- Empty State -->
      <div
        v-else
        class="tb-empty-state"
      >

        <i class="fa-solid fa-mountain"></i>

        <h3>
          Treks coming soon
        </h3>

        <p>
          We're preparing some incredible trails for you.
        </p>

      </div>

    </div>

  </section>


  <!-- ================= WHY TRAILBLAZE ================= -->
  <section id="about" class="tb-about-section">

    <div class="tb-section-container">


      <div class="tb-about-heading">

        <span class="tb-section-label">
          WHY TRAILBLAZE
        </span>

        <h2>
          Built for the trail.
        </h2>

        <p>
          Everything you need to discover, plan and
          experience your next adventure.
        </p>

      </div>


      <div class="tb-feature-grid">


        <!-- Feature 01 -->
        <div class="tb-feature">

          <span class="tb-feature-number">
            01
          </span>

          <div class="tb-feature-icon">

            <i class="fa-solid fa-mountain"></i>

          </div>

          <h3>
            Remarkable trails
          </h3>

          <p>
            Explore carefully selected trekking
            experiences across India's most beautiful
            landscapes.
          </p>

        </div>


        <!-- Feature 02 -->
        <div class="tb-feature">

          <span class="tb-feature-number">
            02
          </span>

          <div class="tb-feature-icon">

            <i class="fa-solid fa-shield-heart"></i>

          </div>

          <h3>
            Trek with confidence
          </h3>

          <p>
            Experience organised adventures with
            experienced staff and clear trek information.
          </p>

        </div>


        <!-- Feature 03 -->
        <div class="tb-feature">

          <span class="tb-feature-number">
            03
          </span>

          <div class="tb-feature-icon">

            <i class="fa-solid fa-calendar-check"></i>

          </div>

          <h3>
            Simple planning
          </h3>

          <p>
            Find a trek, check the details and start
            planning your next adventure in minutes.
          </p>

        </div>

      </div>

    </div>

  </section>


  <!-- ================= STATISTICS ================= -->
  <section class="tb-stats-section">

    <div class="tb-section-container">


      <div class="tb-stats-intro">

        <span class="tb-section-label">
          TRAILBLAZE
        </span>

        <h2>
          Made for explorers.
        </h2>

      </div>


      <div class="tb-stats-grid">


        <div class="tb-stat">

          <strong>
            100+
          </strong>

          <span>
            Happy Trekkers
          </span>

        </div>


        <div class="tb-stat">

          <strong>
            50+
          </strong>

          <span>
            Trekking Experiences
          </span>

        </div>


        <div class="tb-stat">

          <strong>
            20+
          </strong>

          <span>
            Experienced Guides
          </span>

        </div>


      </div>

    </div>

  </section>


  <!-- ================= FINAL CTA ================= -->
  <section class="tb-cta-section">

    <div class="tb-cta-content">

      <span class="tb-section-label">
        YOUR NEXT ADVENTURE
      </span>


      <h2>
        The mountains<br />
        are waiting.
      </h2>


      <p>
        Find a trail that feels like yours.
      </p>


      <router-link
        to="/register"
        class="tb-primary-btn"
      >

        Start exploring

        <i class="fa-solid fa-arrow-right"></i>

      </router-link>

    </div>

  </section>


  <!-- ================= FOOTER ================= -->
  <Footer />

</template>


<script setup>

import "../assets/css/landing.css"

import Footer from "../components/Footer.vue"

import { ref, onMounted } from "vue"

import axios from "axios"


const treks = ref([])


const loadTreks = async () => {

  try {

    const response = await axios.get(
      "http://127.0.0.1:5000/public-treks",
      {
        headers: {
          Authorization:
            "Bearer " +
            localStorage.getItem("token")
        }
      }
    )


    treks.value =
      response.data.treks.slice(0, 3)

  }

  catch (error) {

    console.log(
      "Unable to load featured treks",
      error
    )

  }

}


onMounted(() => {

  loadTreks()

})

</script>