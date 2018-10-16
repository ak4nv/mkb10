export default {
  items: [], // here the notifications will be added

  add (notification) {
    notification.id = Date.now()
    this.items.push(notification)
  },
  remove (notification) {
    this.items = this.items.filter(el => el !== notification)
  },
  clean () {
    if (this.items.length) {
      this.items = this.items.filter(el => typeof el.delay !== 'undefined')
    }
  }
}
