FROM node:24-alpine

WORKDIR /app

RUN npm install -g pnpm

COPY package*.json pnpm-lock.yaml ./

RUN pnpm install

COPY . .

EXPOSE 3030

CMD ["pnpm", "exec", "slidev", "--open", "--remote"] 