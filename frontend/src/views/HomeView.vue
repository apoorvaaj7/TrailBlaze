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
      <div class="container text-center text-white">
        <h1 class="display-3 fw-bold">
          Explore Beyond Limits
        </h1>
        <p class="lead my-4">
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
</template>

<script setup>

import "../assets/css/landing.css"

</script>