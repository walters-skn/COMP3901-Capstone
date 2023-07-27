
<template>
    <h2> User List Admin View</h2>
    <table>
        <thead>
            <tr>
                <th> Patient ID</th>
                <th> First Name</th>
                <th> Last Name</th>
                <th> Email </th>
                <th> Patient Contact Number</th>
                <th> Nutritional Level</th>
                <th> Reminder Type</th>
                <th> Medication Name</th>
                <th> Commencement Date</th>
                <th> Termindation Date</th>
                <th> Clinic Name</th>
                <th> Appointment Date</th>
                <th> Appointment Reminder</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td> {{  }}</td>
                <td> {{  }}</td>
                <td> {{  }}</td>
                <td> {{  }}</td>
                <td> {{  }}</td>
                <td> {{  }}</td>
                <td> {{  }}</td>
                <td> {{  }}</td>
                <td> {{  }}</td>
                <td> {{  }}</td>
                <td> {{  }}</td>
                <td> {{  }}</td>
                <td> {{  }}</td>
            </tr>
        </tbody>
    </table>
</template>

<script>

export default{
    data(){
        return{

        };
    },
    mounted(){
        fetch('*endpoint*')
        .then(response => response.json())
        .then(data => {
            this.users = data;
        })
        .catch(error => {
            console.error('Error fetching user data:', error);
        })
    }
}
</script>

<style scoped>

</style>
