#Build stage
FROM node:16-alpine

WORKDIR /app
COPY server/package.json .
COPY server/package-lock.json .
RUN npm install
COPY server/. .

ENV HACKERS_PIN=5678037569

EXPOSE 3000
CMD sed -i "s/REDACTED/$HACKERS_PIN/" owners.json && sed -i "s/FLAG/1221 Bowery St, Brooklyn, NY 11224, USA. $FLAG/" owners.json && npx ts-node index.ts

