/*
 * @Description: Task Store
 * @Version: 1
 * @Author: Taki Guan
 * @Date: 2021-02-06 22:32:57
 * @LastEditors: Taki Guan
 * @LastEditTime: 2021-02-06 22:47:25
 */
export const state = () => ({
  list: [{ text: 'Test Task', done: false }],
})

export const mutations = {
  add(state, text) {
    state.list.push({
      text,
      done: false,
    })
  },
  remove(state, { todo }) {
    state.list.splice(state.list.indexOf(todo), 1)
  },
  toggle(state, todo) {
    todo.done = !todo.done
  },
}
