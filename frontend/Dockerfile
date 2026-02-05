FROM node:18
WORKDIR /app
COPY . .
RUN npm install && npm run build
FROM nginx
COPY --from=0 /app/dist /usr/share/nginx/html
