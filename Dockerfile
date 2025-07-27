FROM node:24-alpine

WORKDIR /app

RUN npm install -g pnpm

COPY package*.json pnpm-lock.yaml ./

RUN pnpm install

COPY . .

EXPOSE 3000

CMD ["pnpm", "exec", "slidev", "--host", "0.0.0.0", "--port", "3000"] 