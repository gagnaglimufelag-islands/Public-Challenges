import { NextResponse } from "next/server";

function genSecureSecret(len) {
  var chars = '';

  while (chars.length < len) {
      chars += Math.random().toString(36).substring(2);
  }

  return chars.substring(0, len);
}

function authenticate(flag_sec) {
  const p = genSecureSecret(34);

  if (flag_sec === p) {
    return true;
  }
  return false;
}

export function middleware(req) {
  const protectedRoutes = ["/flag"];

  const searchParams = req.nextUrl.searchParams
  const flag_sec = searchParams.get("flag_secret")

  if (protectedRoutes.includes(req.nextUrl.pathname) && !authenticate(flag_sec)) {
    return NextResponse.redirect(new URL("/worthy", req.url));
  }

  return NextResponse.next();
}