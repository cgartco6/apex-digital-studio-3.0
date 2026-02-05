export default function adminGuard(to, from, next) {
  const role = localStorage.getItem('role')
  if (role === 'admin') next()
  else next('/dashboard')
}
