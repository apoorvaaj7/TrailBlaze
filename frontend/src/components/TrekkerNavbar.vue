<template>

    <nav class="navbar navbar-expand-lg navbar-dark bg-success fixed-top shadow">
        <div class="container">
            <router-link
                to="/dashboard" class="navbar-brand fw-bold">
                <i class="fa-solid fa-mountain me-2"></i>
                TrailBlaze
            </router-link>
            <button class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbar">
                <span class="navbar-toggler-icon"></span>
            </button>
            &nbsp; &nbsp;
            <router-link class="nav-link" to="/dashboard">
                Dashboard
            </router-link>
            <div class="collapse navbar-collapse" id="navbar">
                <div class="mx-auto d-flex">
                    <input v-model="search" class="form-control" placeholder="Search Trek or Location..." style="width:300px;"
                        @keyup.enter="searchTreks">
                    <select v-model="difficulty" class="form-select ms-2" placeholder="Filter difficulty" style="width:170px;">
                        <option>All</option>
                        <option>Easy</option>
                        <option>Moderate</option>
                        <option>Hard</option>
                    </select>
                    <button class="btn btn-light ms-2" @click="searchTreks">
                        <i class="fa-solid fa-magnifying-glass"></i>
                    </button>
                </div>
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <router-link to="/my-treks" class="nav-link">
                            My Treks
                        </router-link>
                    </li>
                    <li class="nav-item ms-3">
                        <button class="btn btn-outline-light" @click="logout">
                            Logout
                        </button>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

</template>

<script setup>

    import { ref } from "vue"
    import { useRouter } from "vue-router"
    const router = useRouter()
    const search = ref("")
    const difficulty = ref("All")

    const searchTreks = ()=>{
        router.push({
            path:"/dashboard",
            query:{
                query:search.value,
                difficulty:difficulty.value
            }
        })
    }

    const logout = () =>{
        localStorage.clear()
        router.push("/login")
    }
</script>