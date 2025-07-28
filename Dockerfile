FROM node:24-alpine

WORKDIR /app

RUN npm install -g pnpm serve

COPY package*.json pnpm-lock.yaml ./

RUN pnpm install

COPY . .

RUN pnpm exec slidev build

EXPOSE 3030

CMD ["serve", "-s", "dist", "-l", "3030"] 