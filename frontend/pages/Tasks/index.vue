<!--
 * @Description: Task Vue File
 * @Version: 1
 * @Author: Taki Guan
 * @Date: 2021-02-06 21:50:53
 * @LastEditors: Taki Guan
 * @LastEditTime: 2021-02-08 11:46:11
-->
<template>
  <v-container>
    <v-row>
      <v-col sm="8" offset-sm="2">
        <h1>Tasks</h1>
        <v-text-field
          v-model="newTask.title"
          label="Enter Task"
          @keypress.enter="addTask"
        ></v-text-field>
        <!-- <v-textarea
          v-model="newTask.description"
          label="Description"
          outlined
        /> -->
        <v-card>
          <v-list dense>
            <v-subheader>Task List</v-subheader>
            <v-list-item-group color="primary">
              <v-list-item v-for="(task, i) in tasks" :key="i">
                <template #default="{ active }">
                  <v-list-item-action>
                    <v-checkbox :input-value="active"></v-checkbox>
                  </v-list-item-action>

                  <v-list-item-content>
                    <span
                      v-if="editingTask.id === task.id"
                      class="d-flex justify-space-between"
                    >
                      <v-text-field
                        v-model="editingTask.title"
                        append-outer-icon="mdi-check"
                        @click:append-outer="saveEdit"
                        @keypress.enter="saveEdit"
                      >
                      </v-text-field>
                      <v-icon @click.stop="cancelEdit">mdi-close-circle</v-icon>
                    </span>
                    <span v-else class="d-flex justify-space-between">
                      {{ task.title }}

                      <span>
                        <v-icon @click.stop="editTask(i)">mdi-pencil</v-icon>
                        <v-icon @click.stop="removeTask(task.id)"
                          >mdi-delete-outline</v-icon
                        >
                      </span>
                    </span>
                  </v-list-item-content>
                </template>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapState, mapMutations, mapActions } from 'vuex'

export default {
  data() {
    return {
      newTask: {
        title: '',
        description: '',
        // TODO
        user: 1,
      },
      editingTask: {},
    }
  },

  computed: {
    ...mapState('tasks', ['tasks']),
  },
  created() {
    this.getAllTasks()
  },
  methods: {
    ...mapMutations('tasks', ['add', 'edit', 'remove', 'toggle']),
    ...mapActions('tasks', [
      'getAllTasks',
      'postNewTask',
      'deleteTask',
      'updateTask',
    ]),
    addTask() {
      this.postNewTask(this.newTask)
      this.newTask = {
        title: '',
        description: '',
        // TODO
        user: 1,
      }
    },
    removeTask(taskID) {
      this.deleteTask(taskID)
    },
    editTask(index) {
      this.editingTask = { ...this.tasks[index] }
    },
    cancelEdit() {
      this.editingTask = {}
    },
    saveEdit() {
      const payload = {
        id: this.editingTask.id,
        task: this.editingTask,
      }
      delete payload.task.id

      this.updateTask(payload)
      this.cancelEdit()
    },
  },
}
</script>

<style></style>
