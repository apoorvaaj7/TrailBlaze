<template>

    <AdminNavbar />

    <div class="container py-5">
        <h2 class="fw-bold mb-4">
            Edit Trek
        </h2>

        <form @submit.prevent="updateTrek">
            <div class="row">
                <div class="col-md-6 mb-3">
                    <label>Trek Name</label>
                    <input v-model="trek_name" class="form-control">
                </div>
                <div class="col-12 mb-3">
                    <label>Description</label>
                    <textarea rows="5" v-model="description" class="form-control"></textarea>
                </div>
                <div class="col-md-6 mb-3">
                    <label>Location</label>
                    <input v-model="location" class="form-control">
                </div>
                <div class="col-md-6 mb-3">
                    <label>Difficulty</label>
                    <select v-model="difficulty" class="form-select">
                        <option>Easy</option>
                        <option>Moderate</option>
                        <option>Hard</option>
                    </select>
                </div>
                <div class="col-md-6 mb-3">
                    <label>Duration (Days)</label>
                    <input type="number" v-model="duration" class="form-control">
                </div>
                <div class="col-md-6 mb-3">
                    <label>Price</label>
                    <input type="number" v-model="price" class="form-control">
                </div>
                <div class="col-md-6 mb-3">
                    <label>Available Slots</label>
                    <input type="number" v-model="available_slots" class="form-control">
                </div>
                <div class="col-md-6 mb-3">
                    <label>Image URL</label>
                    <input v-model="image_url" class="form-control">
                </div>
                <div class="col-md-6 mb-3">
                    <label>Staff</label>
                    <select v-model="staff_id" class="form-select">
                        <option v-for="staff in staffs" :key="staff.id" :value="staff.id">
                            {{ staff.full_name }}
                        </option>
                    </select>
                </div>
                <div class="col-md-6 mb-3">
                    <label>Start Date</label>
                    <input type="date" v-model="start_date" class="form-control">
                </div>
                <div class="col-md-6 mb-3">
                    <label>End Date</label>
                    <input type="date" v-model="end_date" class="form-control">
                </div>
            </div>
            <button type="submit" class="btn btn-success">
                Update Trek
            </button>
        </form>
    </div>

<Footer />
</template>

<script setup>

    import { ref,onMounted } from "vue"
    import axios from "axios"
    import { useRouter,useRoute } from "vue-router"
    import AdminNavbar from "../components/AdminNavbar.vue"
    import Footer from "../components/Footer.vue"

    const router = useRouter()
    const route = useRoute()

    const trek_name = ref("")
    const description = ref("")
    const location = ref("")
    const difficulty = ref("")
    const duration = ref("")
    const price = ref("")
    const image_url = ref("")
    const available_slots = ref("")
    const staff_id = ref("")
    const start_date = ref("")
    const end_date = ref("")

    const staffs = ref([])

    const loadStaff = async()=>{
        const response = await axios.get("http://127.0.0.1:5000/admin/staff",
            {
                headers:{
                    Authorization:"Bearer "+localStorage.getItem("token")
                }
            })

        staffs.value = response.data.staff
    }
    const loadTrek = async()=>{
        const response = await axios.get(`http://127.0.0.1:5000/admin/treks/${route.params.id}`,
            {
                headers:{
                    Authorization:"Bearer "+localStorage.getItem("token")
                }
            })
        const trek = response.data.trek

        trek_name.value = trek.trek_name
        description.value = trek.description
        location.value = trek.location
        difficulty.value = trek.difficulty
        duration.value = trek.duration
        price.value = trek.price
        image_url.value = trek.image_url
        available_slots.value = trek.available_slots
        staff_id.value = trek.staff_id
        start_date.value = trek.start_date
        end_date.value = trek.end_date
    }
    const updateTrek = async()=>{
        try{
            const response = await axios.patch(`http://127.0.0.1:5000/admin/treks/${route.params.id}`,
                {
                    trek_name: trek_name.value,
                    description: description.value,
                    location: location.value,
                    difficulty: difficulty.value,
                    duration: duration.value,
                    price: price.value,
                    image_url: image_url.value,
                    available_slots: available_slots.value,
                    staff_id: staff_id.value,
                    start_date: start_date.value,
                    end_date: end_date.value
                },
                {
                    headers:{
                        Authorization:"Bearer "+localStorage.getItem("token")
                    }
                })
            alert(response.data.message)
            router.push("/admin/manage-treks")
        }
        catch(error){
            alert(error.response.data.message)
        }
    }
    onMounted(() => {
        loadStaff()
        loadTrek()
    })

</script>